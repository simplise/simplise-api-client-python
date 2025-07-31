"""JsonLogic action helpers for Simplise API."""

from .types import ActionParams, JsonLogicRule, JsonValue


def to_json_logic(value: ActionParams) -> JsonLogicRule:
    """Convert ActionParams to JsonLogicRule.

    Args:
        value: Value to convert

    Returns:
        JsonLogicRule representation
    """
    # [AI GENERATED] Convert various parameter types to JsonLogic format
    if value is None:
        return {"null": []}
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, bool):
        return {"bool": [str(value)]}
    # Assume it's already a JsonLogicRule
    return value # type: ignore[return-value]


def to_json_logic_value(value: JsonValue) -> JsonLogicRule:
    """Convert JsonValue to JsonLogicRule.

    Args:
        value: JSON value to convert

    Returns:
        JsonLogicRule representation
    """
    # [AI GENERATED] Convert JSON values to JsonLogic format with proper type handling
    if value is None:
        return {"null": []}
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, bool):
        return {"bool": [str(value)]}
    if isinstance(value, list):
        return {"arr": [to_json_logic_value(item) for item in value]}
    if isinstance(value, dict):
        entries: list[JsonLogicRule] = []
        for key, val in value.items():
            entries.append(to_json_logic_value(key))
            entries.append(to_json_logic_value(val))
        return {"obj": entries}
    return str(value)


class DecimalActions:
    """High-precision decimal arithmetic actions."""

    @staticmethod
    def add(*values: ActionParams) -> JsonLogicRule:
        """Addition operation.

        Args:
            *values: Values to add

        Returns:
            JsonLogic rule for addition
        """
        # [AI GENERATED] Create decimal addition rule
        return {"decimal.add": [to_json_logic(val) for val in values]}

    @staticmethod
    def sub(*values: ActionParams) -> JsonLogicRule:
        """Subtraction operation.

        Args:
            *values: Values to subtract (left to right)

        Returns:
            JsonLogic rule for subtraction
        """
        # [AI GENERATED] Create decimal subtraction rule
        return {"decimal.sub": [to_json_logic(val) for val in values]}

    @staticmethod
    def mul(*values: ActionParams) -> JsonLogicRule:
        """Multiplication operation.

        Args:
            *values: Values to multiply

        Returns:
            JsonLogic rule for multiplication
        """
        # [AI GENERATED] Create decimal multiplication rule
        return {"decimal.mul": [to_json_logic(val) for val in values]}

    @staticmethod
    def div(*values: ActionParams) -> JsonLogicRule:
        """Division operation.

        Args:
            *values: Values to divide (left to right)

        Returns:
            JsonLogic rule for division
        """
        # [AI GENERATED] Create decimal division rule
        return {"decimal.div": [to_json_logic(val) for val in values]}

    @staticmethod
    def mod(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Modulo operation.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            JsonLogic rule for modulo
        """
        # [AI GENERATED] Create decimal modulo rule
        return {"decimal.mod": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def pow(base: ActionParams, exponent: ActionParams) -> JsonLogicRule:
        """Power operation.

        Args:
            base: Base value
            exponent: Exponent value

        Returns:
            JsonLogic rule for power
        """
        # [AI GENERATED] Create decimal power rule
        return {"decimal.pow": [to_json_logic(base), to_json_logic(exponent)]}

    @staticmethod
    def abs(value: ActionParams) -> JsonLogicRule:
        """Absolute value.

        Args:
            value: Input value

        Returns:
            JsonLogic rule for absolute value
        """
        # [AI GENERATED] Create decimal absolute value rule
        return {"decimal.abs": [to_json_logic(value)]}

    @staticmethod
    def round(value: ActionParams, precision: ActionParams = 0) -> JsonLogicRule:
        """Round to specified precision.

        Args:
            value: Value to round
            precision: Number of decimal places

        Returns:
            JsonLogic rule for rounding
        """
        # [AI GENERATED] Create decimal rounding rule
        return {"decimal.round": [to_json_logic(value), to_json_logic(precision)]}

    @staticmethod
    def min(*values: ActionParams) -> JsonLogicRule:
        """Minimum value.

        Args:
            *values: Values to compare

        Returns:
            JsonLogic rule for minimum
        """
        # [AI GENERATED] Create decimal minimum rule
        return {"decimal.min": [to_json_logic(val) for val in values]}

    @staticmethod
    def max(*values: ActionParams) -> JsonLogicRule:
        """Maximum value.

        Args:
            *values: Values to compare

        Returns:
            JsonLogic rule for maximum
        """
        # [AI GENERATED] Create decimal maximum rule
        return {"decimal.max": [to_json_logic(val) for val in values]}

    @staticmethod
    def between(
        value: ActionParams, min_val: ActionParams, max_val: ActionParams, inclusive: bool = True
    ) -> JsonLogicRule:
        """Check if value is between min and max.

        Args:
            value: Value to check
            min_val: Minimum value
            max_val: Maximum value
            inclusive: Whether to include boundaries

        Returns:
            JsonLogic rule for between check
        """
        # [AI GENERATED] Create decimal between range check rule
        op = "decimal.between" if inclusive else "decimal.between_exclusive"
        return {op: [to_json_logic(value), to_json_logic(min_val), to_json_logic(max_val)]}


class StringActions:
    """String manipulation actions."""

    @staticmethod
    def concat(*values: ActionParams) -> JsonLogicRule:
        """String concatenation.

        Args:
            *values: Values to concatenate

        Returns:
            JsonLogic rule for concatenation
        """
        # [AI GENERATED] Create string concatenation rule
        return {"str.concat": [to_json_logic(val) for val in values]}

    @staticmethod
    def upper(value: ActionParams) -> JsonLogicRule:
        """Convert to uppercase.

        Args:
            value: String value

        Returns:
            JsonLogic rule for uppercase conversion
        """
        # [AI GENERATED] Create string uppercase rule
        return {"str.upper": [to_json_logic(value)]}

    @staticmethod
    def lower(value: ActionParams) -> JsonLogicRule:
        """Convert to lowercase.

        Args:
            value: String value

        Returns:
            JsonLogic rule for lowercase conversion
        """
        # [AI GENERATED] Create string lowercase rule
        return {"str.lower": [to_json_logic(value)]}


class ArrayActions:
    """Array manipulation actions."""

    @staticmethod
    def filter(array: ActionParams, condition: ActionParams) -> JsonLogicRule:
        """Filter array elements.

        Args:
            array: Array to filter
            condition: Filter condition

        Returns:
            JsonLogic rule for array filtering
        """
        # [AI GENERATED] Create array filter rule
        return {"filter": [to_json_logic(array), to_json_logic(condition)]}

    @staticmethod
    def map(array: ActionParams, transform: ActionParams) -> JsonLogicRule:
        """Map array elements.

        Args:
            array: Array to map
            transform: Transform function

        Returns:
            JsonLogic rule for array mapping
        """
        # [AI GENERATED] Create array map rule
        return {"map": [to_json_logic(array), to_json_logic(transform)]}


class Action:
    """JsonLogic Rule execution system action helpers."""

    @staticmethod
    def input(key: str) -> JsonLogicRule:
        """Get input value by key.

        Args:
            key: Input key

        Returns:
            JsonLogic rule for input access
        """
        # [AI GENERATED] Create input access rule
        return {"input": [key]}

    @staticmethod
    def obj(value: JsonValue) -> JsonLogicRule:
        """Create object literal.

        Args:
            value: Object value

        Returns:
            JsonLogic rule for object
        """
        # [AI GENERATED] Create object literal rule
        return to_json_logic_value(value)

    @staticmethod
    def bool_value(value: bool) -> JsonLogicRule:
        """Create boolean literal.

        Args:
            value: Boolean value

        Returns:
            JsonLogic rule for boolean
        """
        # [AI GENERATED] Create boolean literal rule
        return {"bool": [str(value)]}

    @staticmethod
    def if_condition(condition: ActionParams, then_value: ActionParams, else_value: ActionParams) -> JsonLogicRule:
        """Conditional logic (if-then-else).

        Args:
            condition: Condition to evaluate
            then_value: Value when condition is true
            else_value: Value when condition is false

        Returns:
            JsonLogic rule for conditional
        """
        # [AI GENERATED] Create conditional logic rule
        return {"if": [to_json_logic(condition), to_json_logic(then_value), to_json_logic(else_value)]}

    @staticmethod
    def and_logic(*conditions: ActionParams) -> JsonLogicRule:
        """Logical AND operation.

        Args:
            *conditions: Conditions to evaluate

        Returns:
            JsonLogic rule for AND operation
        """
        # [AI GENERATED] Create logical AND rule
        return {"and": [to_json_logic(cond) for cond in conditions]}

    @staticmethod
    def or_logic(*conditions: ActionParams) -> JsonLogicRule:
        """Logical OR operation.

        Args:
            *conditions: Conditions to evaluate

        Returns:
            JsonLogic rule for OR operation
        """
        # [AI GENERATED] Create logical OR rule
        return {"or": [to_json_logic(cond) for cond in conditions]}

    @staticmethod
    def not_logic(condition: ActionParams) -> JsonLogicRule:
        """Logical NOT operation.

        Args:
            condition: Condition to negate

        Returns:
            JsonLogic rule for NOT operation
        """
        # [AI GENERATED] Create logical NOT rule
        return {"not": [to_json_logic(condition)]}

    @staticmethod
    def eq(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Equality comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for equality
        """
        # [AI GENERATED] Create equality comparison rule
        return {"==": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def ne(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Inequality comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for inequality
        """
        # [AI GENERATED] Create inequality comparison rule
        return {"!=": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def gt(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Greater than comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for greater than
        """
        # [AI GENERATED] Create greater than comparison rule
        return {">": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def gte(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Greater than or equal comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for greater than or equal
        """
        # [AI GENERATED] Create greater than or equal comparison rule
        return {">=": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def lt(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Less than comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for less than
        """
        # [AI GENERATED] Create less than comparison rule
        return {"<": [to_json_logic(a), to_json_logic(b)]}

    @staticmethod
    def lte(a: ActionParams, b: ActionParams) -> JsonLogicRule:
        """Less than or equal comparison.

        Args:
            a: First value
            b: Second value

        Returns:
            JsonLogic rule for less than or equal
        """
        # [AI GENERATED] Create less than or equal comparison rule
        return {"<=": [to_json_logic(a), to_json_logic(b)]}

    decimal = DecimalActions
    str = StringActions
    array = ArrayActions



# Add decimal actions to Action class
# Action.decimal = DecimalActions
# Action.str = StringActions
# Action.array = ArrayActions
