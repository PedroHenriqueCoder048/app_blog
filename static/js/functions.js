async function RetornaBlogs() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/blogs', {
      method: 'GET'
    });

    if (!response.ok) {
      throw new Error(`Erro HTTP: ${response.status}`);
    }

    const jsonData = await response.json();
    return jsonData

  } catch (error) {
    console.error('Erro ao buscar blogs:', error);
  }
};

