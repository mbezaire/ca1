top -p `pgrep $1 | head -n20 | tr "\n" "," | sed 's/,$//'` -n1 -b | tail -n$2 | head -n$3
