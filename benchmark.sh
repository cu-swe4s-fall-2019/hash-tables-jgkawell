python hash_functions.py --input_file rand_words.txt --hash_function ascii | python scatter.py --out_file ascii_hash_function_rand.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input_file rand_words.txt --hash_function rolling | python scatter.py --out_file rolling_hash_function_rand.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input_file non_rand_words.txt --hash_function ascii | python scatter.py --out_file ascii_hash_function_non_rand.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input_file non_rand_words.txt --hash_function rolling | python scatter.py --out_file rolling_hash_function_non_rand.png --x_label "Hashed word" --y_label "Hashed value"

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_alg ascii --collision_strategy linear --data_file_name rand_words.txt --keys_to_add $M >  ascii_linear_rand.$M.txt
done

grep insert ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file linear_insert_time.png --x_label "Load factor" --y_label "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search ascii_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py --out_file ascii_search_time.png --x_label "Load factor" --y_label "Search time"

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_alg rolling --collision_strategy linear --data_file_name rand_words.txt --keys_to_add $M >  rolling_linear_rand.$M.txt
done

grep insert rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_insert_time.png --x_label "Load factor" --y_label "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search rolling_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py --out_file rolling_search_time.png --x_label "Load factor" --y_label "Search time"
