module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    // publicPath: process.env.NODE_ENV === 'development' ? '/' : './',
    proxy: {
      '/api': {
        target: 'http://192.168.120.130:8000',
        changeOrigin: true,
      },
    }
  }
}