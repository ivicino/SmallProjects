# Camera detection

import cv2
from pyzbar.pyzbar import decode
import pandas as pd

Data = []

cascPath = ".\\Downloads\\xmlClassifiers\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()   # ret is a boolean that is True when video is on
    

    # Barcode script__________________________________________
    detectedBarcodes = decode(frame)    # Detects the barcode

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
        
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
            
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(frame, (x-10, y-10),
                        (x + w+10, y + h+10),
                        (255, 0, 0), 2)
            
            if barcode.data!="":
            
            # Print the barcode data
                print(f'Barcode Data: {barcode.data}')

                if barcode.data == b'505278':
                    Data.append('Geeks')
                elif barcode.data == b'0123023':
                    Data.append('IanIsTheGreatestScientist')
                elif barcode.data == b'0822014':
                    Data.append('Karina = Scientist')
                elif barcode.data == b'0070048778193':
                    Data.append('Karina')
                
                    
                
                print(Data)

                Datadf = pd.DataFrame(Data)

                print(barcode.type)
                print("\n \n You scanned a barcode! \n CONGRATULATIONS \n \n ")

        # break

    # Barcode script__________________________________________

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # Breaks the loop when the user clicks the letter Q.
        break
# When everything is done, release the capture

writer = pd.ExcelWriter('pandasEx.xlsx', 
                   engine ='xlsxwriter')

Datadf.to_excel(writer, sheet_name ='Sheet1')


writer.save()

video_capture.release()
cv2.destroyAllWindows()

df = pd.DataFrame(pd.read_excel('pandasEx.xlsx'))
print(df.head(20))