# hydra on shell


```bash

# create alias and ws server

$ source activate.sh

# sources can be piped to effects

$ osc | repeat 2 2

# pipe to out to send to javascript side

$ osc | repeat 2 2 | out 

# for [].fast use fast alias

$ osc `fast 2 2 2` | repeat 2 3 | out

# use redirect for source income (just some functions allow it)

$ voronoi | modulate `noise 0.2 2` | out
$ voronoi | modulate <<< `noise 0.2 2` | out

# for js functions:

$ osc 't => Math.sin(3*t)/2' 2 | out

# TEST if it's possible

# create a FIFO socket file

$ mkfifo freq
$ osc @freq 2 3 | out  # will read from fifo tail till Control + C 


# in other terminal

while true
do
    echo $RANDOM > freq
done




```

on hydra side:

```javascript


```
