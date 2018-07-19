# Generated from ObjectiveCParser.g4 by ANTLR 4.7.1
from antlr4 import *


# This class defines a complete generic visitor for a parse tree produced by ObjectiveCParser.

class ObjectiveCParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ObjectiveCParser#translationUnit.
    def visitTranslationUnit(self, ctx):
        print('Running Codegen...')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#topLevelDeclaration.
    def visitTopLevelDeclaration(self, ctx):
        print ctx.getRuleIndex()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#importDeclaration.
    def visitImportDeclaration(self, ctx):
        pass

    # Visit a parse tree produced by ObjectiveCParser#classInterface.
    def visitClassInterface(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#categoryInterface.
    def visitCategoryInterface(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#classImplementation.
    def visitClassImplementation(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#categoryImplementation.
    def visitCategoryImplementation(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#genericTypeSpecifier.
    def visitGenericTypeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolDeclaration.
    def visitProtocolDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolDeclarationSection.
    def visitProtocolDeclarationSection(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolDeclarationList.
    def visitProtocolDeclarationList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#classDeclarationList.
    def visitClassDeclarationList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolList.
    def visitProtocolList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertyAttributesList.
    def visitPropertyAttributesList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertyAttribute.
    def visitPropertyAttribute(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolName.
    def visitProtocolName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#instanceVariables.
    def visitInstanceVariables(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#visibilitySection.
    def visitVisibilitySection(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#accessModifier.
    def visitAccessModifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#interfaceDeclarationList.
    def visitInterfaceDeclarationList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#classMethodDeclaration.
    def visitClassMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#instanceMethodDeclaration.
    def visitInstanceMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#implementationDefinitionList.
    def visitImplementationDefinitionList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#classMethodDefinition.
    def visitClassMethodDefinition(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#instanceMethodDefinition.
    def visitInstanceMethodDefinition(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#methodDefinition.
    def visitMethodDefinition(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#methodSelector.
    def visitMethodSelector(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#keywordDeclarator.
    def visitKeywordDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#selector.
    def visitSelector(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#methodType.
    def visitMethodType(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertyImplementation.
    def visitPropertyImplementation(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertySynthesizeList.
    def visitPropertySynthesizeList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#propertySynthesizeItem.
    def visitPropertySynthesizeItem(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#blockType.
    def visitBlockType(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#genericsSpecifier.
    def visitGenericsSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeSpecifierWithPrefixes.
    def visitTypeSpecifierWithPrefixes(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#dictionaryExpression.
    def visitDictionaryExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#dictionaryPair.
    def visitDictionaryPair(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#arrayExpression.
    def visitArrayExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#boxExpression.
    def visitBoxExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#blockParameters.
    def visitBlockParameters(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeVariableDeclaratorOrName.
    def visitTypeVariableDeclaratorOrName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#blockExpression.
    def visitBlockExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#messageExpression.
    def visitMessageExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#receiver.
    def visitReceiver(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#messageSelector.
    def visitMessageSelector(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#keywordArgument.
    def visitKeywordArgument(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#keywordArgumentType.
    def visitKeywordArgumentType(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#selectorExpression.
    def visitSelectorExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#selectorName.
    def visitSelectorName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolExpression.
    def visitProtocolExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#encodeExpression.
    def visitEncodeExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeVariableDeclarator.
    def visitTypeVariableDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#throwStatement.
    def visitThrowStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#tryBlock.
    def visitTryBlock(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#catchStatement.
    def visitCatchStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#autoreleaseStatement.
    def visitAutoreleaseStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#functionSignature.
    def visitFunctionSignature(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attribute.
    def visitAttribute(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeName.
    def visitAttributeName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeParameters.
    def visitAttributeParameters(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeParameterList.
    def visitAttributeParameterList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeParameter.
    def visitAttributeParameter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeParameterAssignment.
    def visitAttributeParameterAssignment(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#varDeclaration.
    def visitVarDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typedefDeclaration.
    def visitTypedefDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeDeclaratorList.
    def visitTypeDeclaratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeDeclarator.
    def visitTypeDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#attributeSpecifier.
    def visitAttributeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#initDeclarator.
    def visitInitDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#ibOutletQualifier.
    def visitIbOutletQualifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#arcBehaviourSpecifier.
    def visitArcBehaviourSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#nullabilitySpecifier.
    def visitNullabilitySpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typePrefix.
    def visitTypePrefix(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeQualifier.
    def visitTypeQualifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#protocolQualifier.
    def visitProtocolQualifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeofExpression.
    def visitTypeofExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#fieldDeclaratorList.
    def visitFieldDeclaratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#fieldDeclarator.
    def visitFieldDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#enumeratorList.
    def visitEnumeratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#enumerator.
    def visitEnumerator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#enumeratorIdentifier.
    def visitEnumeratorIdentifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#directDeclarator.
    def visitDirectDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#declaratorSuffix.
    def visitDeclaratorSuffix(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#parameterList.
    def visitParameterList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#pointer.
    def visitPointer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#macro.
    def visitMacro(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#arrayInitializer.
    def visitArrayInitializer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#structInitializer.
    def visitStructInitializer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#initializerList.
    def visitInitializerList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#typeName.
    def visitTypeName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#abstractDeclaratorSuffix.
    def visitAbstractDeclaratorSuffix(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#parameterDeclarationList.
    def visitParameterDeclarationList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#declarator.
    def visitDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#labeledStatement.
    def visitLabeledStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#rangeExpression.
    def visitRangeExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#compoundStatement.
    def visitCompoundStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#selectionStatement.
    def visitSelectionStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#switchStatement.
    def visitSwitchStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#switchBlock.
    def visitSwitchBlock(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#switchSection.
    def visitSwitchSection(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#switchLabel.
    def visitSwitchLabel(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#iterationStatement.
    def visitIterationStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#whileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#doStatement.
    def visitDoStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#forStatement.
    def visitForStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#forLoopInitializer.
    def visitForLoopInitializer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#forInStatement.
    def visitForInStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#jumpStatement.
    def visitJumpStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#expressions.
    def visitExpressions(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#castExpression.
    def visitCastExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#initializer.
    def visitInitializer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#constantExpression.
    def visitConstantExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#unaryOperator.
    def visitUnaryOperator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#postfixExpression.
    def visitPostfixExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#postfix.
    def visitPostfix(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#argumentExpression.
    def visitArgumentExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ObjectiveCParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)
