import React from 'react';
import { Paper } from '@material-ui/core';

class CursoHolder extends React.Component{
    
    render(){
        return(
            <h1>{this.props.titulo}</h1>
        );
    };
}

export default CursoHolder;