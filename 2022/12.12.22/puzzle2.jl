using DelimitedFiles
using Graphs

input = reduce(vcat, permutedims.(collect.(open(readdlm, "input.txt"))))

start = findfirst(isequal('S'), input)
dest = findfirst(isequal('E'), input)

# use unicode representation to convert chars to ints
m = map(x -> Int(x) - 96, input)
m[start] = 1
m[dest] = 26

rows = size(m)[1]
cols = size(m)[2]
start_vertex = rows * (start[2] - 1) + start[1]
dest_vertex = rows * (dest[2] - 1) + dest[1]

g = SimpleDiGraph(rows * cols)
ct = 1
potential_starts = []
for i in CartesianIndices(m)
    if m[i] == 1
        push!(potential_starts, ct)
    end
    if ct > rows && m[CartesianIndices(m)[ct-rows]] <= m[i] + 1
        add_edge!(g, ct, ct - rows)
    end
    if ct <= cols * rows - rows && m[CartesianIndices(m)[ct+rows]] <= m[i] + 1
        add_edge!(g, ct, ct + rows)
    end
    if ct % rows != 1 && m[CartesianIndices(m)[ct-1]] <= m[i] + 1
        add_edge!(g, ct, ct - 1)
    end
    if ct % rows != 0 && m[CartesianIndices(m)[ct+1]] <= m[i] + 1
        add_edge!(g, ct, ct + 1)
    end
    global ct += 1
end

shortest = dijkstra_shortest_paths(g, start_vertex).dists[dest_vertex]
for i in potential_starts
    d = dijkstra_shortest_paths(g, i).dists[dest_vertex]
    if d < shortest
        global shortest = d
    end
end

println(shortest)