from pyzbar.pyzbar import decode
import numpy as np
import cv2
import json


def readqr(frame,detections):
        """
        Reading the QR Codes on frame.
        :return: Return inside the QR data as a result.
        """
        for barcode in decode(frame):
                myData = barcode.data.decode('utf-8')
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(frame,[pts],True,(255,0,255),5)
                pts2 = barcode.rect
                cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)
                if myData in detections:
                    print("The QR Code has been readen before.")
                    
                    return False
                return myData
            
            
def görev_sonucu(data,start_time,end_time):
    pass 

cap = cv2.VideoCapture(0)
success_detects = []

while cap.isOpened():
    
    ret, frame = cap.read()        
    height, width, channels = frame.shape
    scale = 416 / max(height, width)
    cv2.resize(frame, (round(scale * width), round(scale * height)))
    
    # QR Koda gitmek için gerekli waypoint ve servo çalışma oranları burada olacak.
    
    data = readqr(frame,success_detects)
    if data is not False and data is not None:
        if data not in success_detects:
            success_detects.append(data)
               
            
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
