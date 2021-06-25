import time
from datetime import datetime

def ping():
	start = datetime.now()
	end = datetime.now()
	m_s = (end - start).microseconds / 1000
	pong = f"<i>Pinged back at </i>{m_s} <i>ms</i>"
	return pong