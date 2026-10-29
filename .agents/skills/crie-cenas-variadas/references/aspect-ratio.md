# Aspect ratio exato

Usar largura e altura reais do arquivo fornecido. Simplificar por máximo divisor comum: 1920×1080 → 16:9, 1080×1920 → 9:16, 1200×900 → 4:3, 1000×667 → 1000:667. Não arredondar para preset por conveniência.

Sem dimensões verificáveis, pedir largura e altura antes de afirmar ratio exato. O script aspect_ratio.py recebe dimensões, valida inteiros positivos e calcula a razão; ele não descobre dimensões de pixels nem garante que um gerador aceite valores incomuns.

Todas as cinco propostas e dez prompts repetem a mesma proporção. Nunca recortar, esticar ou mudar orientação para acomodar o enquadramento. Se o gerador não suporta ratio, declarar limitação em vez de dizer que preservou o original.
