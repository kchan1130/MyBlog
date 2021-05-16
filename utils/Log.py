import os
import datetime
import logging
from logging import StreamHandler
# from logging.handlers import RotatingFileHandler


Log = logging.getLogger()
Log.setLevel(logging.DEBUG)

'''
Handler实例
    StreamHandler**: 输出 LogRecord 到类似于 sys.stdout、sys.stderr 之类的流中，
                     或者是任何的类文件对象（file-like object)。
    FileHandler**: 继承自 StreamHandler 输出功能，将 LogRecord 输出到硬盘文件中。
    SocketHandler**: 内置在 logging.handler 模块中，输出 LogRecord 到网络套接字上，
                     默认使用的是 TCP 套接字。
    DatagramHandler**: 内置在 logging.handler 模块中，继承自 SocketHandler 输出功能，
                       但是通过 UDP 套接字发送报文信息。
    SysLogHandler**: 内置在 logging.handler 模块中，输出 LogRecord 到远程
                     或本地的 Unxi 系统日志当中（Unix syslog）
    SMTPHandler**: 内置在 logging.handler 模块中，通过 SMTP 协议输出 LogRecord 到电子邮箱地址。
    HTTPHandler**: 内置在 logging.handler 模块中，输出 LogRecord 到 Web 服务器上，
                   支持 GET 和 POST 方法。在 Python 3.5 中新增了 context 参数。
'''
sh = StreamHandler()
if not os.path.exists('hislog'):
    os.mkdir('hislog')
logpath = os.path.join('hislog', f'{datetime.date.today()}.log')
# fh = RotatingFileHandler(logpath, maxBytes=10*1024*1024, backupCount=5)

# 配置格式 添加到handler
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s %(filename)s::%(funcName)s::L%(lineno)d %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
sh.setFormatter(formatter)
# fh.setFormatter(formatter)

# logger添加 handler
Log.addHandler(sh)
# Log.addHandler(fh)
