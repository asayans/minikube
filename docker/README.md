# Flask users Docker image

Aplicacion Flask minima para listar, crear y eliminar usuarios guardados en una base de datos SQLite local.

## Construir la imagen

```powershell
docker build -t flask-users .
```

## Ejecutar el contenedor

```powershell
docker run --rm -p 5000:5000 -v users-data:/data flask-users
```

Abre `http://localhost:5000`.

La base de datos se guarda en `/data/users.db`. El volumen `users-data` conserva los usuarios aunque se recree el contenedor.

## Configuracion opcional

Puedes cambiar la conexion de base de datos con `DATABASE_URL`:

```powershell
docker run --rm -p 5000:5000 -e DATABASE_URL=sqlite:////data/users.db -v users-data:/data flask-users
```
