# Installation und Setup

Die Implementierung der Objekterkennungsmodelle, mit Ausnahme von YOLOv5, erfolgt mithilfe der TensorFlow 2 Object Detection API. Um sicherzustellen, dass die Entwicklungsumgebung unter Windows 11 korrekt eingerichtet ist, sind einige wichtige Installationsschritte zu beachten. Ein zentrales Element dabei ist die Installation der `Protobuf`-Bibliothek, die in einer passenden Version vorliegen muss.

Falls bereits eine Version von Protobuf installiert ist, empfiehlt es sich, diese zunächst zu deinstallieren und anschließend die `Protobuf`-Bibliothek erneut über Conda zu installieren:

```bash
$ pip uninstall protobuf
$ conda install protobuf

Da die standardmäßige Installation der Protobuf-Bibliothek unter Umständen die Datei builder.py nicht enthält, muss diese manuell heruntergeladen und im entsprechenden Verzeichnis abgelegt werden:

$ curl https://raw.githubusercontent.com/protocolbuffers/protobuf/main/python/google/protobuf/internal/builder.py \
  > <PathToYourInstallation>\google\protobuf\internal\builder.py

Nach der Installation und Sicherstellung der Kompatibilität zwischen Protobuf und TensorFlow 2 können die nächsten Schritte gemäß der offiziellen Dokumentation durchgeführt werden. Dazu gehört unter anderem das Klonen des TensorFlow-OD Repositories:

import os
import pathlib

if "models" in pathlib.Path.cwd().parts:
  while "models" in pathlib.Path.cwd().parts:
    os.chdir('..')
elif not pathlib.Path('models').exists():
  !git clone --depth 1 https://github.com/tensorflow/models


Anschließend muss die Protobuf-Kompilierung für die Objekterkennungsprotokolle durchgeführt werden. Dies geschieht, indem man in das .models/research Verzeichnis des geklonten Repositories wechselt und die Kompilierung ausführt:

import subprocess
import shutil

os.chdir('./models/research')
subprocess.run(['protoc', 'object_detection/protos/*.proto', '--python_out=.'], shell=True, check=True)
shutil.copy('object_detection/packages/tf2/setup.py', '.')
subprocess.run(['python', '-m', 'pip', 'install', '.'], shell=True, check=True)

Die erfolgreiche Installation und Kompatibilität von TensorFlow und Protobuf kann durch die Ausführung des Model-Builders überprüft werden:

$ python object_detection/builders/model_builder_tf2_test.py


Abschließend zur TensorFlow Installation werden die Zufallszahlengeneratoren auf feste Werte gesetzt, um reproduzierbare Ergebnisse während der Modellimplementierung sicherzustellen:

import random
import numpy as np
import tensorflow as tf

random.seed(42)
np.random.seed(42)
tf.compat.v1.random.set_random_seed(42)

Für die Installation von YOLOv5 von Ultralytics wurden keine nennenswerten Abweichungen von den Schritten der offiziellen Dokumentation vorgenommen, sodass diese problemlos als Leitfaden verwendet werden können.
