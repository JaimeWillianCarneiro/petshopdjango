from django.db import models

# Create your models here.



class usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=12)
    



class cliente(models.Model):
    id = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)


class fornecedor(models.Model):
    id = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)




class pedido(models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    nome =  models.CharField(max_length=50)
    especieDestinada = models.CharField(max_length=30)
    preco = models.FloatField(max_length=50)
    
    
    
class compra(models.Model):
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    enderecodestino = models.CharField(max_length= 70)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_cliente', 'id_pedido'], name='nique_id_cliente_id_pedido_combination'
            )
        ]
    

    
    
class fornece(models.Model):
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_cliente', 'id_pedido'], name='nique_id_cliente_id_pedido_combination'
            )
        ]
    
    
class produto(models.Model):
    quantidade = models.IntegerField(255)
    marca = models.CharField(max_length= 50)
    validade = models.DateField()
    # id_produto = models.ForeignKey(produto, )
    


class servico(models.Model):
    id_servico = models.BigAutoField(primary_key=True)
    id_servico = models.ForeignKey(pedido, on_delete=models.CASCADE)
    duracao = models.CharField(max_length= 20)
    local = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    



