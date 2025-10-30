# TROCAR-CVLAN-OLT-FIBERHOME
## Visão Geral
Script em Python 3 para cadastrar/trocar a CVLAN de ONU na OLT Fiberhome. 


### Bibliotecas Necessárias
Para o funcionamento correto do script baixe as bibliotecas
<p>
  <a href="https://pysimplegui.readthedocs.io/en/latest/">🔗 PySimpleGUI</a>
<p>
  <a href="https://docs.python.org/3/library/telnetlib.html">🔗 telnetlib</a>
</p>
<p>
  <a href="https://docs.python.org/3/library/time.html">🔗 time</a>
  
### Interface Gráfica
<p>
    Insira o IP da sua OLT Fiberhome e escolha o Slot e a porta PON;
</p>
  
 ![figura1](https://user-images.githubusercontent.com/46397610/130873914-4aaf7e85-9a1f-4a91-9966-3e2c2d6c5bd6.png)

<p>
    Em seguida informe um valor númerico para a TAG Vlan e se deve ser alterada ou cadastrada; 
</p>

 ![figura2](https://user-images.githubusercontent.com/46397610/130874461-5a9ed7b3-1fa9-4f51-8a3d-03c27a54ee49.png)

<p>
    Aqui você indica qual o Slot e a porta PON que as ONU estão autorizadas.
</p> 
<p>
    Repare que na barra de rolagem você indica qual o intervalo de ONU a ser manipulado, neste caso serão alteradas da 4 até a 14 em um total de 10 ONU;
</p>

 ![figura3](https://user-images.githubusercontent.com/46397610/130876491-5f33c223-c036-422c-ba3f-44820d5a9678.png)

<p>
    Por fim informe o usuário e senha que você utiliza no UNM2000 e clique em executar.
</p>

 ![figura4](https://user-images.githubusercontent.com/46397610/130877166-61a67ca8-f482-4433-94b1-0f8d83a472cd.png)

<p>
    Todas as ONU alteradas serão reinicializadas. Se desejar impedir que isso aconteça basta comentar as linhas com o comando:
</p>
<p>
    terminal.write(reset.encode('ascii') + b"\n")
</p>

 ![figura4](https://user-images.githubusercontent.com/46397610/130880342-27d5d6b6-4cc3-4c01-becb-df5ab42bb5b9.gif)


### Contribuindo
Desde de já agradeço por se disponibilizarem a contribuir com melhorias para este script. Todos podem ajudar este projeto com novos recursos, correções de bugs ou melhorias de desempenho.
