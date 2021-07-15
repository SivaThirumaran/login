import logging as L

def log(level,message,file):
    L.basicConfig(level=L.INFO,filename=file, filemode="a",
                  format="%(asctime)s %(levelname)s %(message)s",
                  datefmt="%d-%m-%y %H:%M:%S")
    if level == "INFO":L.info(message)
    if level == "WARNING": L.warning(message)
    if level == "ERROR": L.error(message)
    if level == "CRITICAL": L.critical(message)