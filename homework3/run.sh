echo ">------------------------------------<"
echo "              Start                   "
echo ">------------------------------------<"
python main.py data/English-train.xml data/English-dev.xml KNN-English.answer SVM-English.answer Best-English.answer English
python main.py data/Spanish-train.xml data/Spanish-dev.xml KNN-Spanish.answer SVM-Spanish.answer Best-Spanish.answer Spanish
python main.py data/Catalan-train.xml data/Catalan-dev.xml KNN-Catalan.answer SVM-Catalan.answer Best-Catalan.answer Catalan
echo ">------------------------------------<"
echo "               End                    "
echo ">------------------------------------<"