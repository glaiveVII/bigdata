
txt() {
cat <<- EOM
  Julien Pelegri
EOM
}


awk 'BEGIN{FS=",";OFS=","} /time/{print $0} !/time/{coupe=$2*10^(-9);date=strftime("%F",coupe);print $1,date,$3,$4,$5,$6,$7,$8,$9,$10,$11,"\n"}' 20190222-dump.csv > sortie_test.csv


 awk '
BEGIN {
    FS=",";
    OFS=","
}
!/time/ {
    coupe=$2*10^(-9);
    date=strftime("%F",coupe);
    print date,$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,"\n" >> date".csv"
}
' 20190222-dump.csv


awk '
BEGIN {
    FS=",";
    OFS=","
}
/time/{print $0} !/time/ {
    coupe=$2*10^(-9);
    date=strftime("%F",coupe);
    print date,$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,"\n"
}
' 20190222-dump.csv \
| awk '
BEGIN {
    FS=",";
    OFS=","
}
{
    print $0 >> "$1.csv"
}
'
