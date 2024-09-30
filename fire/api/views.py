from rest_framework import views, response


class SavePoint(views.APIView):

    def post(self, request, *args, **kwargs):

        print('*'*200)

        return response.Response({

        }, status=200)
