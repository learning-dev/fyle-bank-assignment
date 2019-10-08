from . serializers import BankDataSerializer
from . models import Bank
from . helpers import bankPagination

from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bank(request):
	ifsc = request.GET.get('ifsc_code')
	bank = Bank.get_bank_by_ifsc(ifsc)
	if bank:
		bank_serilizer = BankDataSerializer(bank)
		return Response(bank_serilizer.data, status=status.HTTP_200_OK)
	else:
		return Response({
			'message':'Error: No such Bank Found for ifsc_code: ' + ifsc  
			}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_branches(request):
	paginator = bankPagination()
	bank_name = request.GET.get('bank').upper()
	city = request.GET.get('city').upper()

	branches = Bank.get_branch_in_city(bank_name, city)
	if branches:
		page = paginator.paginate_queryset(branches, request)
		bank_serilizer = BankDataSerializer(page, many=True)
		return paginator.get_paginated_response(bank_serilizer.data)
	else:
		return Response({
			'message': 'Error: No such branch Found!'
			}, status=status.HTTP_404_NOT_FOUND)

