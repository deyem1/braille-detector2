import streamlit as st

try:
    from tensorflow.keras.models import load_model
    # import cv2
    import cv2
    import tensorflow as tf
    # import os



    import numpy as np
    import pandas as pd

    st.title('Braille Detector:book:')
    # img_file_buffer = st.camera_input("Take a picture")


    def predict_upload():

        resize = tf.image.resize(cv2_imgg, (256, 256))
        print('got here4')

        yhat = new_model.predict(np.expand_dims(resize / 255, 0))
        print(yhat)

        if yhat > 0.5:
            st.error('Predicted class is not braille :thumbsdown:')
        else:
            st.success('Predicted class is Braille :thumbsup:')

    # if img_file_buffer is not None:
    #     st.image(img_file_buffer)
    #     # To read image file buffer with OpenCV:
    #     bytes_data = img_file_buffer.getvalue()
    #     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    #     new_model = load_model("G:\My Drive\Colab Notebooks\braille detector\models\brailleclassifier1.h5",
    #                            compile=False)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        print('got here0')
        bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)
        print('got here1')
        # bytes_data = bytes_data.getvalue()
        print('got here 1.5')
        cv2_imgg = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        print('got here2')
        new_model = load_model('brailleclassifierr1.h5',
                               compile=False)
        print('got here2')



        trigger = st.button('Predict', on_click=predict_upload)
    else:
        print('no image')
        #
    # if img_file_buffer is not None:
    #     st.image(img_file_buffer)
    #     # To read image file buffer with OpenCV:
    #     bytes_data = img_file_buffer.getvalue()
    #     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    #     new_model = load_model("G:\My Drive\Colab Notebooks\image classification\model\imageclassifier1.h5",
    #                            compile=False)
    #
    #
    #     def predict():
    #         # print(type(cv2_img))
    #         # print(st.write(type(cv2_img)))
    #
    #         # img = cv2.imread(cv2_img)
    #         resize = tf.image.resize(cv2_img, (256, 256))
    #         yhat = new_model.predict(np.expand_dims(resize / 255, 0))
    #         print(yhat)
    #         # yhat = new_model.predict(np.expand_dims(cv2_img / 255, 0))
    #         if yhat > 0.5:
    #             st.error('Predicted class is Sad :thumbsdown:')
    #         else:
    #             st.success('Predicted class is Happy :thumbsup:')
    #
    #
    #     trigger = st.button('Predict', on_click=predict)
    # else:
    #     print('no image')
        #
except:
    print('i thoeu')


