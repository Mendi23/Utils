// function component (rcf<e>)
const Comp = (props) => {
    return (<>JSX</>)
}

export default Comp

// PropTypes (impt)
import PropTypes from 'prop-types'
Comp.defaultProps = {
    title: 'default value'
}

Comp.propTypes = {
    title: PropTypes.string,
    head: PropTypes.string.isRequired
}


// styling
const compStyle = {
    color: 'red',
    backgroudColor: 'black'
} // inside JSX: <dic style={compStyle}>
// class = className