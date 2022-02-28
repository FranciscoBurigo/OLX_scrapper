# OLX web scraping 

<p align="center">
 <a href = "#sobre">Sobre</a>.
 <a href = "#tecnologias">Tecnologias</a>.
 <a href = "#pre-requisitos">Pré-requisitos</a>.
 <a href = "#autor">Autor</a>.
</p>

<br>

<h4 align="center">
	✔️ PROJETO README ✔️ Finalizado ✔️

</h4>

# Sobre

Aquisição de dados de anuncios de terrenos no site [olx](https://www.olx.com.br/) para Florianópolis e região. 
Obtendo os dados e assim fazendo um análise de de dados basica, podendo comparar preços e ofertas por região.

#Pré-requisitos

Antes de começar, é importante ter instalado em sua máquina as seguintes ferramentas:
[Git](https://gitforwindows.org/), [Pyhton](https://www.python.org/downloads/), navegador [google chrome](https://www.google.com/intl/pt_br/chrome/)
e o drive para conseguir acessar pelo código [chromedriver](https://chromedriver.chromium.org/downloads), ele já está no repositório, mas dependendo da versão do google chrome pode ser necessário 
baixar outra versão. Além disso é bom ter um editor para trabalhar no projeto. Após instalar o [Pyhton](https://www.python.org/downloads/) é necessário instalar 
algumas bibliotecas que não são nativas.

### Instalando Bibliotecas
```bash
#Instalar pelo terminal/cmd
$py -m pip install selenium

#Instalar pelo terminal/cmd
$py -m pip install request

#Instalar pelo terminal/cmd
$py -m pip install pandas

#Instalar pelo terminal/cmd
$py -m pip install bs4

#Instalar pelo terminal/cmd
$py -m pip install datetime

#Instalar pelo terminal/cmd
$py -m pip install lxml

#Instalar pelo terminal/cmd
$py -m pip install unidecode
```

### Rodando o código
```bash

# Clona o repositótio 
$git clone https://github.com/FranciscoBurigo/OLX_scrapper.git

#Acesse a pasta do projeto(nome de sua escolhe da pasta) pelo terminal--cmd
$cd OLX_scrapper_clone

#Execute a aplicação
$Buscador_de_dados_olx.py
```

Para observar a analise realizada pode ser acessada por:

-[Planilha Dados](https://docs.google.com/spreadsheets/d/1FTeiU782t_PxD4oidL8YhtBN_wfLkXTyzRbDgEfBlIQ/edit?usp=sharing)

Ou caso preferir pode puxar ela da pasta e utilizar, mas pode ser perdido algum dado ou analise devido a importação.

Caso deseje acesso para editar, enviar e-mail para: franciscoburigo@gmail.com.


### 💻 Tecnologias Utilizadas

As principais ferramentes utilizadas no projeto foram:

- [Pyhton](https://www.python.org/downloads/)
- [chromedriver](https://chromedriver.chromium.org/downloads)
- [Google sheets](https://www.google.com/sheets/about/)

### Autor

Feito por Francisco Burigo 💚 [Acesse meu Linkedin](https://www.linkedin.com/in/franciscoburigo/)

