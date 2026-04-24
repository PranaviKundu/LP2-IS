import java.security.MessageDigest;
import java.math.BigInteger;

public class MD5Example {
    public static void main(String[] args) {
        try {
            String input = "Hello World";
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);
            String hashtext = no.toString(16);
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
            System.out.println("Input: " + input);
            System.out.println("MD5 Digest: " + hashtext.toUpperCase());
        } catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }
}