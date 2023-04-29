import queue
import time
import numpy as np
import cv2 as cv
from func import routing_node_mission

qimg = queue.Queue(3)

qimg.put([12,23,34,45])
qimg.put([34,23,34,45])
qimg.put([56,23,34,45])
# qimg.put([56,23,34,45], timeout=0.1)

def foo(dat, dat2):
    print('dat', dat, dat2)
    time.sleep(5)
    print('dat2', dat, dat2)


if __name__ == '__main__':
    d = queue.Queue(3)
    e = queue.Queue(3)
    d.put('dd1')
    d.put('dd2')
    e.put('e1')
    e.put('e2')
    print(d.qsize(), e.qsize())

    d = d+e
    print(d.qsize(), e.qsize())

    exit()

    Mask = 255 * np.ones((100, 100, 3), dtype=np.int)
    Mask = np.array(Mask, dtype='uint8')
    cv.arrowedLine(Mask, (0, 0), (80, 80), (0, 0, 255), 2, line_type=cv.LINE_4, shift=0, tipLength=0.1)  #line_type=cv.LINE_4,)
    cv.imshow('dfd', Mask)
    cv.waitKey()
    exit()

    rate = 1e-5
    test = routing_node_mission.Routing_Node_CPU(id='101', num_class=4, generate_rate=rate, recv_rate=rate
                                                 , processing_rate=rate*10, max_data_size=5, send_buf=100,
                                                 recv_buf=100, build_Thread=None)

    test.node_generate_data_thread()


