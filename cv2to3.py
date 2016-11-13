try: # import opencv if necessary
    cv2
except NameError:
    import cv2

def is_cv2():
    return cv2.__version__[0] == '2'

def is_cv3():
    return cv2.__version__[0] == '3'

# Compatibility fix for OpenCV < 3.0
if (cv2.__version__[0] == '2') or (not cv2.__version__[0] == '3'):
    # map all cv2.cv.CV_* to cv2.*
    for key, value in cv2.cv.__dict__.items():
        if key.startswith('CV_'):
            setattr(cv2, key[3:], value)
    # fix some specific changes
    cv2.VideoWriter_fourcc = cv2.cv.CV_FOURCC
