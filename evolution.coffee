SEQ_LEN = 7
SEQ_MAX = 100
POP_SIZE = 4

randint = (min, max) ->
    Math.floor(Math.random() * (max - min + 1) + min)

  rand_sequence = ->
    [randint(0, SEQ_MAX) for i in [0...SEQ_LEN]]

  mutate = (sequence) ->
    rand_index = randint(0, SEQ_LEN - 1)
    [randint(0, SEQ_MAX) if index is rand_index else x for x, index in sequence]

    alert rand_sequence()
    alert mutate(rand_sequence())
