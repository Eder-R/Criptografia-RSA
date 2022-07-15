import (
	"bufio"
	b64 "encoding/base64"
	"log"
	"math/big"
	"os"
	"rsago/utils"
)

func main() {
	// leitura da chave publica
	keyFileName := os.Args[1]
	// Leitura do arquivo a ser criptografado
	srcFileName := os.Args[2]
	// Leitura da criptografia a ser realizada
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

	originalEncodedText := ""

	srcFile, err := os.Open(srcFileName)
	if err != nil {
		log.Fatalln(err)
	}
	defer func(srcFile *os.File) {
		_ = srcFile.Close()
	}(srcFile)

	srcFileScanner := bufio.NewScanner(srcFile)

	for srcFileScanner.Scan() {
		line := srcFileScanner.Text()
		encodedChunk, _ := new(big.Int).SetString(line, 10)
		originalChunk := encodedChunk.Exp(encodedChunk, key, modulus)

		base64EncodedChunk := utils.NewBigInt(originalChunk).Text()

		originalEncodedText += base64EncodedChunk
	}

	decryptedTextBytes, _ := b64.StdEncoding.DecodeString(originalEncodedText)
	decryptedText := string(decryptedTextBytes)

	_, err = dstWriter.WriteString(decryptedText)
	if err != nil {
		log.Fatalln(err)
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
