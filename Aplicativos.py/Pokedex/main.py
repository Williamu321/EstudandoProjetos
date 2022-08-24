<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokédex</title>

    <link rel="stylesheet" href="./src/css/reset.css">
    <link rel="stylesheet" href="./src/css/global.css">
    <link rel="stylesheet" href="./src/css/cartao.css">
    <link rel="stylesheet" href="./src/css/listagem.css">
    <link rel="stylesheet" href="./src/css/responsivo.css">
    
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;800&display=swap" rel="stylesheet">

</head>

<body>
    <main>
        <div class="pokedex">
            <div class="cartoes-pokemon">
                <div class="cartao-pokemon aberto tipo-eletrico" id="cartao-pikachu">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Pikachu</h2>
                            <span>#025</span>
                        </div>
                        <span class="tipo">elétrico</span>

                        <div class="cartao-imagem">
                            <img src="./src/images/pikachu.png" alt="Imagem do Pikachu">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 300</li>
                                <li>Ataque: 600</li>
                                <li>Defesa: 500</li>
                                <li>Velocidade: 300</li>
                                <li>Total: 1.700</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Choque do trovão</li>
                                <li>Cabeçada</li>
                            </ul>

                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-grama" id="cartao-bulbasaur">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Bulbasaur</h2>
                            <span>#001</span>
                        </div>
                        <span class="tipo">grama</span>

                                <div class="cartao-imagem">
                                    <img src="./src/images/bulbasaur.png" alt="Imagem do Bulbasaur">
                                </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 320</li>
                                <li>Ataque: 510</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 200</li>
                                <li>Total: 1.430</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Folhas navalha</li>
                                <li>Raio solar</li>
                            </ul>

                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-fogo" id="cartao-charmander">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Charmander</h2>
                            <span>#004</span>
                        </div>
                        <span class="tipo">fogo</span>

                        <div class="cartao-imagem">
                            <img src="./src/images/charmander.png" alt="Imagem do Charmander">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 200</li>
                                <li>Ataque: 300</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 320</li>
                                <li>Total: 1.220</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Lança-chamas</li>
                                <li>Ataque rápido</li>
                            </ul>

                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-agua" id="cartao-gyarados">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Gyarados</h2>
                            <span>#130</span>
                        </div>
                        <span class="tipo">água</span>

                        <div class="cartao-imagem">
                            <img src="./src/images/gyarados.png" alt="Imagem do Gyarados">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 300</li>
                                <li>Ataque: 600</li>
                                <li>Defesa: 500</li>
                                <li>Velocidade: 300</li>
                                <li>Total: 1.700</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Jato d'Água</li>
                                <li>Hidro bomba</li>
                            </ul>

                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-trevas" id="cartao-gengar">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Gengar</h2>
                            <span>#094</span>
                        </div>
                        <span class="tipo">trevas</span>

                        <div class="cartao-imagem">
                            <img src="./src/images/gengar.png" alt="Imagem do Gengar">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 100</li>
                                <li>Ataque: 200</li>
                                <li>Defesa: 300</li>
                                <li>Velocidade: 400</li>
                                <li>Total: 1.000</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Bola sombria</li>
                                <li>Lambida</li>
                            </ul>

                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-dragao" id="cartao-dragonite">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Dragonite</h2>
                            <span>#149</span>
                        </div>
                        <span class="tipo">dragão</span>

                        <div class="cartao-imagem">
                            <img src="./src/images/dragonite.png" alt="Imagem do Dragonite">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 500</li>
                                <li>Ataque: 600</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 400</li>
                                <li>Total: 1.900</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Dança do dragão</li>
                                <li>Velocidade extrema</li>
                            </ul>

                        </div>
                    </div>
                </div>

            </div>

            <nav class="listagem">

                <ul>
                    <li class="pokemon ativo" id="pikachu">
                        <img src="./src/images/cabeca-pikachu.png" alt="Cabeça do Pikachu">
                        <span>Pikachu</span>
                    </li>

                    <li class="pokemon" id="bulbasaur">
                        <img src="./src/images/cabeca-bulbasaur.png" alt="Cabeça do Bulbasaur">
                        <span>Bulbasaur</span>
                    </li>

                    <li class="pokemon" id="charmander">
                        <img src="./src/images/cabeca-charmander.png" alt="Cabeça do Charmander">
                        <span>Charmander</span>
                    </li>

                    <li class="pokemon" id="gyarados">
                        <img src="./src/images/cabeca-gyarados.png" alt="Cabeça do Gyarados">
                        <span>Gyarados</span>
                    </li>

                    <li class="pokemon" id="gengar">
                        <img src="./src/images/cabeca-gengar.png" alt="Cabeça do Gengar">
                        <span>Gengar</span>
                    </li>

                    <li class="pokemon" id="dragonite">
                        <img src="./src/images/cabeca-dragonite.png" alt="Cabeça do Dragonite">
                        <span>Dragonite</span>
                    </li>
                </ul>

            </nav>

        </div>

    </main>

    <script src="./src/js/index.js"></script>
</body>


