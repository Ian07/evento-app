import React from 'react'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Button from '@material-ui/core/Button'
import Typography from '@material-ui/core/Typography'

const Curso = (props) => {
  console.log(props)
  return(
      <div>
          { props.curso ? (
              <Card>
                  <CardMedia style={{height:0, paddingTop: '56.25%'}}
                  image={props.curso.imagen}
                  title={props.curso.nombre}
                  />
                  <CardContent>
                  <Typography gutterBottom variant="h5" component="h2">
                    {props.curso.nombre}
                  </Typography>
                  <Typography variant="body2" color="textSecondary" component="p">
                    {props.curso.descripcion}
                  </Typography>
                  <Typography variant="body2" color="textSecondary" component="p">
                    {props.curso.slogan}
                  </Typography>
                  </CardContent>
                  <CardActions>
                      <Button size="small" color="primary" href="#" target="_blank">
                          Inscribirseee
                      </Button>
                  </CardActions>
              </Card>
          ) : <h1> Hola :D </h1>}
      </div>
  )
}

export default Curso