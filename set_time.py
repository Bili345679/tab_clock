import ctypes
from datetime import datetime, timedelta

# 定义 SYSTEMTIME 结构
class SYSTEMTIME(ctypes.Structure):
    _fields_ = [
        ("wYear", ctypes.c_uint16),
        ("wMonth", ctypes.c_uint16),
        ("wDayOfWeek", ctypes.c_uint16),
        ("wDay", ctypes.c_uint16),
        ("wHour", ctypes.c_uint16),
        ("wMinute", ctypes.c_uint16),
        ("wSecond", ctypes.c_uint16),
        ("wMilliseconds", ctypes.c_uint16)
    ]

def set_system_time(time_str):
    # 将字符串解析为 datetime 对象
    local_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    # 将本地时间转换为 UTC 时间
    utc_time = local_time - timedelta(hours=8)  # 假设本地时区是 UTC+8

    # 设置新的系统时间
    new_time = SYSTEMTIME()
    new_time.wYear = utc_time.year
    new_time.wMonth = utc_time.month
    new_time.wDay = utc_time.day
    new_time.wHour = utc_time.hour
    new_time.wMinute = utc_time.minute
    new_time.wSecond = utc_time.second
    new_time.wMilliseconds = int(utc_time.microsecond / 1000)

    # 调用 Windows API 函数设置系统时间
    ctypes.windll.kernel32.SetSystemTime(ctypes.byref(new_time))

# 示例：设置系统时间为 2024-12-31 23:59:59
set_system_time("2024-12-31 23:59:00")
