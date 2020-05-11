import cv2


def webcam_stream(preview_name, camID):
    cap = cv2.VideoCapture(0)
    i = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            #img = cv2.resize(img, (0, 0), fx=1, fy=1)
            cv2.namedWindow(f"{preview_name}_{camID}",
                            cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
            cv2.imshow(f"{preview_name}_{camID}", img)
            cv2.imwrite(f'./images/image_{camID}_{i}.bmp', img)
            i += 1
            if cv2.waitKey(10) == ord('q'):
                print('break')
                break
        else:
            break


def camera_stream(preview_name, camID):
    """Harvesters"""
    h = Harvester()
    h.add_cti_file('/opt/mvIMPACT_Acquire/lib/x86_64/mvGenTLProducer.cti')
    h.update_device_info_list()
    ia = h.create_image_acquirer(camID)
    #ia.device.node_map.PixelFormat.value = 'BayerRG8'
    #ia.device.node_map.TestPattern = 'HorizontalColorBar'
    time.sleep(5)
    try:
        ia.start_image_acquisition()
        i = 0
        done = False

        while not done:
            with ia.fetch_buffer() as buffer:
                img = buffer.payload.components[0].data
                img = img.reshape(
                    buffer.payload.components[0].height, buffer.payload.components[0].width)
                img_copy = img.copy()
                img_copy = cv2.cvtColor(img, cv2.COLOR_BayerRG2RGB)

                if i == 0:
                    first = img_copy.copy()

                is_change = np.allclose(first, img_copy, 3)
                # print(is_change)
                if not is_change:

                    # cv2.namedWindow("window", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
                    # cv2.imshow("window", img_copy)
                    cv2.imwrite(f'./images/image_{i}.png', img_copy)
                    # img_copy = cv2.resize(img_copy, (640, 480))

                first = img_copy.copy()

                if cv2.waitKey(10) == ord('q'):
                    fps = ia.statistics.fps
                    print("FPS: ", fps)
                    done = True
                    print('break')
                i = i + 1
                # if i == 200:
                #     break
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
    finally:
        ia.stop_image_acquisition()
        ia.destroy()
        print('fin')
        h.reset()


if __name__ == "__main__":
    webcam_stream('webcam', 0)
