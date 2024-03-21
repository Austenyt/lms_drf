from rest_framework import serializers

from users.models import Payment, User, Subscription


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'payments')


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, instance):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=instance).exists()

    class Meta:
        model = Subscription
        fields = ('is_subscribed',)