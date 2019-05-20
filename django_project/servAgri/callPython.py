from .quickIndex import QuickIndex as i
from django.http import HttpResponse, StreamingHttpResponse
import io
from wsgiref.util import FileWrapper

def get_index(request, indexid):
    idx = [indexid]
    red_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif"
    nir_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif"

    qi = i(idx, red = red_file, nir = nir_file)
    output = io.BytesIO()
    response = StreamingHttpResponse(FileWrapper(\
        open("D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\\django_project\\servAgri\\output\\ndvi-image.png"\
            , "rb"), 8192), content_type="image/png")
    return response
    
def ndvi_img(request):
    return HttpResponse("<img src='/ndvi/img'>")

def post_file(self=None):
    f = "D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\\django_project\\servAgri\\output\\test.txt"
    open(f, 'w')

if __name__ == '__main__':
    # get_index()
    post_file()