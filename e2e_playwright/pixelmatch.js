import fs from 'fs';
import { PNG } from 'pngjs';
import pixelmatch from 'pixelmatch';

async function compareImages(basePath, vrcPath, diffPath, options = {
    threshold: 0.1,
    includeAA: true,
    alpha: 0.1,
    aaColor: [255, 0, 0],  // Color para anti-aliasing
    diffColor: [255, 0, 255]  // Color para las diferencias
}) {
    try {
        // Leer las imágenes
        const img1 = PNG.sync.read(fs.readFileSync(basePath));
        const img2 = PNG.sync.read(fs.readFileSync(vrcPath));

        const { width, height } = img1;
        const diff = new PNG({ width, height });

        // Comparar imágenes usando Pixelmatch con las opciones personalizadas
        const numDiffPixels = pixelmatch(
            img1.data,
            img2.data,
            diff.data,
            width,
            height,
            options
        );

        // Guardar el resultado del diff
        fs.writeFileSync(diffPath, PNG.sync.write(diff));

        console.log(`Diferencias encontradas: ${numDiffPixels} píxeles`);
    } catch (error) {
        console.error(`Error al comparar imágenes: ${error.message}`);
    }
}

// Obtener argumentos desde la línea de comandos (basePath, vrcPath, diffPath)
const [,, basePath, vrcPath, diffPath] = process.argv;
compareImages(basePath, vrcPath, diffPath);
