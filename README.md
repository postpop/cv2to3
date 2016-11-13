# cv2to3
Fixes 95% of the compatibility issues between opencv2 and opencv3. This is done by remapping some of the API in opencv2 to the new, opencv3 style. Now, code written targeting opencv3 will work with the opencv2 as well. 

Cases in which the function signatures have been changed (e.g. `cv2.kmeans`) are impossible to fix with this simple remapping approach. Detection of the current opencv version is facilitated using the added convenience functions `is_cv2()` and `is_cv3()`.

These things have been fixed - use the opencv3 version even if you run opencv2:

| x              | opencv2             | opencv3                  |
| -------------: | :-----------------: | :----------------------: |
| property names | `cv2.cv.CV_*`       | `cv2.*`                  |
| fourcc         | `cv2.cv.CV_FOURCC`  | `cv2.VideoWriter_fourcc` |


