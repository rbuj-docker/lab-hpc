```
docker compose build pandas
docker compose run -it --rm -v ${PWD}/files:/home/hpc pandas python3 test.py
```

```
docker compose build rockylinux
docker compose run -it --rm -v ${PWD}/files:/home/hpc rockylinux gnuplot errorbars1.gnu
docker compose run -it --rm -v ${PWD}/files:/home/hpc rockylinux gnuplot errorbars2.gnu
```

```
docker compose run -it --rm -v ${PWD}/files:/home/hpc texlive pdflatex report.tex
```

```
$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED             SIZE
lab-hpc-pandas       latest    8f5960676aec   59 minutes ago      197MB
lab-hpc-rockylinux   latest    b8ed0ffd949a   About an hour ago   559MB
texlive/texlive      latest    f896c9e4652c   37 hours ago        5.14GB
```

https://www.geeksforgeeks.org/use-pandas-to-calculate-stats-from-an-imported-csv-file/
