from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import GroupMessageEvent, PrivateMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.exception import MatcherException
from nonebot.typing import T_State
from nonebot import on_message
import httpx
from .utils.constants import CacheConstants
from .utils.log import log
from .utils.cache import save_cache, load_cache, cache_exists
from .ocr import online_ocr, local_ocr


matcher = on_message(
    priority=10,
    block=False
)


@matcher.handle()
async def handle_message(
    event: GroupMessageEvent,
    state: T_State
):
    if event.post_type == "message":
        getmsg = event.message
        ocr_result = ""
        raw_text = ""
        full_text = ""
        ocr_bool = False
        text_bool = False
        # log.debug(f"{getmsg}")
        for segment in getmsg:
            if segment.type == "image":

                # 获取图片标识信息
                image_name = segment.data.get("file", "")
                image_url = segment.data.get("url", "")
                if not image_name or not image_url:
                    log.error(f"无法获取图片信息: {segment}")
                    await matcher.finish()
                    return

                # 图片数据的缓存键
                image_data_cache_key = f"{CacheConstants.QQ_RAW_PICTURE}{image_name}"
                # OCR结果的缓存键
                ocr_result_cache_key = f"{CacheConstants.OCR_RESULT_TEXT}{image_name}"

                # 先检查缓存中是否有结果
                if cache_exists(ocr_result_cache_key):
                    cached_result = load_cache(ocr_result_cache_key)
                    if cached_result:
                        log.info(f"使用缓存的OCR结果: {image_name}")
                        log.debug(f"缓存的OCR结果: {cached_result}")
                        ocr_result = cached_result
                    else:
                        log.error("缓存存在但无法获取/不该出现")
                        await matcher.finish()
                        return

                # 没有缓存，进行识别
                else:
                    if cache_exists(image_data_cache_key):
                        image_data = load_cache(image_data_cache_key)
                    else:
                        async with httpx.AsyncClient() as client:
                            response = await client.get(image_url)
                            if response.status_code != 200:
                                log.error(
                                    f"获取图像失败，状态码: {response.status_code}")
                                await matcher.finish()
                                return
                            image_data = response.content
                            save_cache(image_data_cache_key, image_data)

                    try:
                        # 尝试使用在线OCR（更可靠）
                        try:
                            ocr_text = local_ocr(
                                image_data, ocr_result_cache_key)
                        except Exception as e:
                            log.warning(f"本地OCR失败: {e}，尝试在线OCR")
                            # 如果在线OCR失败，尝试本地OCR
                            ocr_text = online_ocr(
                                image_data, ocr_result_cache_key)
                    except Exception as e:
                        log.error(f"OCR识别失败: {e}")
                        await matcher.finish()
                        return
                    ocr_result = ocr_text
                if ocr_result:
                    full_text += ocr_result
                    ocr_bool = True
                    log.debug(f"OCR识别结果: {ocr_result}")

            elif segment.type == "text":
                raw_text = segment.data.get("text", "").strip()
                if raw_text:
                    full_text += raw_text
                    text_bool = True
                    log.debug(f"原始文本消息: {raw_text}")

            else:
                log.debug(f"未知消息类型: {segment}{segment.type}")
        state["full_text"] = full_text
        if ocr_bool and text_bool:
            state["ocr_or_text"] = "both"
        elif ocr_bool:
            state["ocr_or_text"] = "ocr"
        elif text_bool:
            state["ocr_or_text"] = "text"
        else:
            log.error("不存在文本或图像识别结果")
        return
    return


@matcher.handle()
async def judge_and_ban(
    event: GroupMessageEvent,
    state: T_State,
    bot: Bot
):
    user_id = event.user_id
    group_id = event.group_id
    full_text = state["full_text"]
    
