module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    // publicPath: process.env.NODE_ENV === 'development' ? '/' : './',
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    }
  }
}