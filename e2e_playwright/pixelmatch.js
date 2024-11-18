const fs = require('fs');
const { createCanvas, loadImage } = require('canvas');
const pixelmatch = require('pixelmatch');

async function compareImages(basePath, vrcPath, diffPath) {
    try {
        const img1 = await loadImage(basePath);
        const img2 = await loadImage(vrcPath);

        const width = img1.width;
        const height = img1.height;

        // Crear un canvas para almacenar la diferencia
        const canvas = createCanvas(width, height);
        const ctx = canvas.getContext('2d');

        // Extraer datos de las imágenes
        ctx.drawImage(img1, 0, 0);
        const img1Data = ctx.getImageData(0, 0, width, height);

        ctx.drawImage(img2, 0, 0);
        const img2Data = ctx.getImageData(0, 0, width, height);

        const diffData = ctx.createImageData(width, height);

        // Comparar imágenes usando Pixelmatch
        const numDiffPixels = pixelmatch(
            img1Data.data,
            img2Data.data,
            diffData.data,
            width,
            height,
            { threshold: 0.1 } // Ajusta el umbral según sea necesario
        );

        // Guardar el resultado del diff
        ctx.putImageData(diffData, 0, 0);
        const buffer = canvas.toBuffer('image/png');
        fs.writeFileSync(diffPath, buffer);

        console.log(`Diferencias encontradas: ${numDiffPixels} píxeles`);
    } catch (error) {
        console.error(`Error al comparar imágenes: ${error.message}`);
    }
}

// Obtener argumentos desde Python
const [,, basePath, vrcPath, diffPath] = process.argv;
compareImages(basePath, vrcPath, diffPath);
