package serpro;

/*
java 11
vanilla request http
*/
import java.net.http.*;
import java.net.http.HttpClient.Version;
import java.net.http.HttpResponse.BodyHandlers;
import java.net.URI;
import java.io.IOException;

class HttpQuery {
    public static void go() throws IOException,InterruptedException  {
        String URL = "https://example.com/test";
        HttpClient client = HttpClient.newBuilder().version(Version.HTTP_2).build();
        HttpRequest request = HttpRequest.newBuilder()
         .uri(URI.create(URL))
         .build();

        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        System.out.println(response.statusCode());
        System.out.println(response.body());
    }

    public static void run() {
        try {
            HttpQuery.go();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}