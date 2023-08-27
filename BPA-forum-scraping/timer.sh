zsh
#!/bin/zsh

start=$(date +%s)

python ./request_image.py 

end=$(date +%s)

echo "Total time: $((end-start)) seconds" 
