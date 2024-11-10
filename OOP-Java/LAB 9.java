import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            String current = new java.io.File( "." ).getCanonicalPath();
            System.out.println("Current dir:"+current);
            List<String> allLines = null;
            String line = scanner.nextLine();
            String regex = "";
            Pattern  pt = null;
            while (!line.equals("Exit")){
                String[] ls = line.split(": ");
                if (ls[0].equals("File") || ls[0].equals("file")){
                    if (ls.length==1){
                        System.out.println("Give me a file to read, not only \"file\" command");
                        break;
                    }
                    allLines = Files.readAllLines(Paths.get(ls[1]));
                    System.out.println("File read...");
                }
                if (ls[0].equals("Regex") || ls[0].equals("regex")){
                    regex = ls[1];
                    pt = Pattern.compile(regex);
                }
                if (ls[0].equals("List") || ls[0].equals("list")){
                    if (allLines!=null) {
                        for (int i = 0; i < allLines.size(); i++) {
                            System.out.println("Line number: "+i+" Line: "+ allLines.get(i));
                        }
                    }
                }
                if (ls[0].equals("Search") || ls[0].equals("search")){
                    if (pt!=null && allLines!=null) {
                        for (int j = 0; j < allLines.size(); j++) {
                            Matcher matc = pt.matcher(allLines.get(j));
                            if (matc.find()) {
                                System.out.print("Line number: "+j+" Matching tokens: ");
                                for (int i = 0; i <= matc.groupCount(); i++) {
                                    System.out.print("\""+matc.group(i)+"\"");
                                }
                                System.out.println("Line: "+allLines.get(j));
                            }
                        }
                    }else {
                        System.out.println("Give regex or file_name to be read to the program.");
                    }
                }
                line = scanner.nextLine();
                }
                scanner.close();
            } catch (IOException e) {
            System.out.println("IOException occured, possibly wrong file name.");;
        }catch (Exception a){
            System.out.println("You got an exception. Quitting...");
        }finally {
            System.out.println("Goodbye :) ...");
        }
        System.out.println("End of main block.");
    }
}

