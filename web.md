## transient vs scoped vs singleton
1. Transient objects are always different; a new instance is provided to every controller and every service.
2. Scoped objects are the same within a request, but different across different requests.
3. Singleton objects are the same for every object and every request.
