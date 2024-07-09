
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Compte
from .serializers import DepotSerializer, RetraitSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

class DepotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        compte = get_object_or_404(Compte, pk=pk)

        # Vérifiez que l'utilisateur authentifié est le propriétaire du compte
        if compte.user != request.user:
            return Response({'detail': 'Non autorisé.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = DepotSerializer(data=request.data)
        if serializer.is_valid():
            try:
                compte.depot(serializer.validated_data['montant'])
                return Response({'solde': compte.solde}, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetraitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        compte = get_object_or_404(Compte, pk=pk)

        # Vérifiez que l'utilisateur authentifié est le propriétaire du compte
        if compte.user != request.user:
            return Response({'detail': 'Non autorisé.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = RetraitSerializer(data=request.data)
        if serializer.is_valid():
            try:
                compte.retrait(serializer.validated_data['montant'])
                return Response({'solde': compte.solde}, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
