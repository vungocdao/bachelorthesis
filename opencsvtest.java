public class opencsvtest
{
    public static void main(String[] args)
    BufferedReader csvReader = new BufferedReader(new FileReader(pathToCsv));
    while ((row = csvReader.readLine()) != null) {
        String[] data = row.split(",");
    }
}
