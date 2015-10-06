public static boolean isValidSudoku(char[][] board) {

    // Check row...
    for(int i = 0; i< 9; i++) {

        HashSet<Character> hash = new HashSet<Character>();

        for(int j = 0; j< 9; j++) {
            char currentChar = board[i][j];
            if (currentChar != '.' && !hash.add(currentChar)) {
                return false;
            }
        }
    }

    // Check column...
    for(int j = 0; j< 9 ; j++) {

        HashSet<Character> hash = new HashSet<Character>();

        for(int i = 0; i< 9; i++) {
            char currentChar = board[i][j];
            if (currentChar != '.' && !hash.add(currentChar)) {
                return false;
            }
        }
    }

    // Check 9x9 grid...
    for(int i = 0; i< 3; i++) {
        for(int j = 0; j< 3; j++) {

            HashSet<Character> hash = new HashSet<Character>();

            for(int ii = i*3; ii< i*3+3; ii++) {
                for(int jj = j*3; jj< j*3+3; jj++){
                    char currentChar = board[ii][jj];
                    if (currentChar != '.' && !hash.add(currentChar)) {
                        return false;
                    }
                }
            }

        }
    }


    return true;
}