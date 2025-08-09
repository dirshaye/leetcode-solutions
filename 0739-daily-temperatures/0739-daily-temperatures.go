func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
    res := make([]int, n)
    stack := make([]int,0, n)

    for i, t := range temperatures {
        for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
            j := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res[j] = i-j
        }
        stack = append(stack,i)
    }
    return res
    
}