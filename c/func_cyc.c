int isOdd(int n) {
    if (n < 2) return n == 1;
    return isEven(n - 1);
}
int isEven(int n) {
    if (n < 2) return n == 0;
    return isOdd(n - 1);
}