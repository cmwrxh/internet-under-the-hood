// Cloudflare Worker: route African traffic to nearest origin
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const country = request.cf.country;
    const continent = request.cf.continent;
    
    // African users → origin with African peering
    if (continent === 'AF') {
      url.hostname = 'origin-af.example.com'; // Johannesburg or Nairobi POP
    } else {
      url.hostname = 'origin-us.example.com';
    }
    
    // Add caching headers for API responses
    const response = await fetch(url, request);
    const newResponse = new Response(response.body, response);
    
    newResponse.headers.set('Cache-Control', 'public, max-age=60, stale-while-revalidate=300');
    newResponse.headers.set('X-Edge-Location', request.cf.colo); // NBO, MBA, JNB
    
    return newResponse;


    
  }
};

