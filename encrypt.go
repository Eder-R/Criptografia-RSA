import (
	b64 "encoding/base64"
	"log"
	"os"
	"rsago/utilgits"
)

func main() {
	// leitura da chave publica
	keyFileName := os.Args[1]
	// Leitura do arquivo a ser descriptografado
	srcFileName := os.Args[2]
	// Leitura da descriptografia a ser realizada
	dstFileName := os.Args[3]

	// abre o arquivo de chaves
	err, keyFileReader := utils.GetKeyFileReader(keyFileName)
	if err != nil {
		log.Fatalln("erro abrindo arquivo de chaves: ", err)
	}

	// abre o arquivo de saída
	err, dstFile, dstWriter := utils.GetDstFileWriter(dstFileName)
	if err != nil {
		log.Fatalln("erro abrindo arquivo de saída: ", err)
	}
	modulus, key := utils.GetKeyFromFile(keyFileReader)

	text := utils.GetTextFromSrcFile(err, srcFileName)

	chunkSize := utils.BlockSize(*modulus)
	codedText := b64.StdEncoding.EncodeToString([]byte(text))

	for _, chunk := range utils.SplitByWidth(codedText, chunkSize) {
		originalChunk := utils.NewString(chunk).BigIntValue()
		encodedChunk := originalChunk.Exp(originalChunk, key, modulus)

		_, _ = dstWriter.WriteString(encodedChunk.Text(10) + "\n")
	}

	err = dstWriter.Flush()
	if err != nil {
		log.Fatalln("Erro ao fazer flush do arquivo de destino.", err)
	}
	err = dstFile.Close()
	if err != nil {
		log.Fatalln("Erro ao fechar o arquivo de destino.", err)
	}
}
